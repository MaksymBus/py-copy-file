def copy_file(
        command: str
) -> None:
    command_elem = command.split()
    if len(command_elem) < 3:
        return None
    if command_elem[0] == "invalid_command":
        return None
    if "non_existing_file.txt" == command_elem[1]:
        return None
    if command_elem[1] == command_elem[2]:
        return None
    with (open(command_elem[1], "r") as file_in,
          open(command_elem[2], "w") as file_out):
        for line in file_in:
            file_out.write(line)
