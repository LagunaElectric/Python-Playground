import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Requires input and output file args.")
        exit()

    input_file_path: str = sys.argv[1]
    output_file_path: str = sys.argv[2]

    if not os.path.isfile(input_file_path):
        print("Input must be a file.")
        exit()

    if os.path.exists(input_file_path):
        lines: list[str] = []
        with open(input_file_path, 'r') as input:
            lines = input.readlines()

        with open(output_file_path, 'w+') as output:
            for line in lines:
                output.write(str(len(line) - 1) + "\n")

    else:
        print("Input must exist.")
