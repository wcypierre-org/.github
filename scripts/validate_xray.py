"""Validate public acceptance identities without private workflows or secrets."""
from pathlib import Path
import re


def validate(root: Path) -> int:
    directory = root / 'xray/acceptance'
    files = sorted(directory.rglob('*.feature'))
    if not 0 < len(files) <= 100:
        raise ValueError('Expected between 1 and 100 acceptance features')
    total = 0
    for path in files:
        if path.is_symlink() or not path.resolve().is_relative_to(directory.resolve()):
            raise ValueError('Feature escapes the acceptance directory')
        tags, identities, scenarios = [], set(), 0
        for line in path.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if line.startswith('@'):
                tags.extend(line.split())
            elif re.match(r'^Scenario(?: Outline| Template)?:', line):
                found = [tag for tag in tags if re.fullmatch(r'@id:[0-9]+', tag)]
                if len(found) != 1 or found[0] in identities:
                    raise ValueError('Each scenario needs a unique @id:number')
                identities.add(found[0])
                scenarios += 1
                tags = []
            elif line and not line.startswith('#'):
                tags = []
        if not scenarios:
            raise ValueError('Feature has no identified scenarios')
        total += scenarios
    return total


if __name__ == '__main__':
    print(f'Validated {validate(Path(__file__).resolve().parents[1])} public acceptance scenarios')
