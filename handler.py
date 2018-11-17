import re
import subprocess


def main(event, context):
    result = subprocess.run(["./splatnet2statink.py", "-r"], encoding="utf-8", stdout=subprocess.PIPE)
    formatted_result = re.sub(r"^splatnet2statink .+\nChecking if there are previously-unuploaded battles...\n", "",
                              result.stdout).strip()
    print(formatted_result)


if __name__ == "__main__":
    main("", "")
