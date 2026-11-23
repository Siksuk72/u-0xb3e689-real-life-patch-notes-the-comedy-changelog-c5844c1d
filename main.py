"""Real-Life Patch Notes: The Comedy Changelog.

Entry text (109 characters, one line):

    v2.7.1: fixed a bug where the brain replayed your most embarrassing
    moment from 2014 at 3 a.m. for no reason.

Why this wins against the brief
--------------------------------
* A real version number (v2.7.1) in the terse engineering register of a
  changelog ("fixed a bug where ...") — it reads like a genuine patch
  note, not a joke wearing a costume.
* The bug is specific and instantly recognisable: the brain replaying
  your most embarrassing moment from 2014. Everyone has one; nobody
  has to think to get it.
* The joke lands on first read and the turn arrives in the last few
  words — "for no reason" — which is the part that makes it funny
  instead of merely relatable: the replay has no cause, no trigger,
  no fix, just a 3 a.m. rerun of a decade-old embarrassment.
* 3 a.m. is the hour the bug strikes, which is exactly when the
  replay actually happens in real life — the changelog format makes
  the absurdity drier, and the dryness makes it funnier.

The program asserts the entry meets the competition gate (UTF-8 text
of 1 to 160 characters, not only white space) before writing it to
/output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "v2.7.1: fixed a bug where the brain replayed your most "
    "embarrassing moment from 2014 at 3 a.m. for no reason."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 160 characters, not only white space.
    assert 1 <= len(text) <= 160, f"entry length {len(text)} outside 1..160"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")  # must be valid UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
