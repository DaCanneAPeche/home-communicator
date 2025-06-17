#!/usr/bin/env python3


from typing import Tuple


def get_is_a_page() -> bool:

    print(
"""
Is it :

[1] A script
[2] A page
"""
    )

    answer : str = input('-> ')

    if answer not in ('1', '2'):
        print(f"Incorrect answer {answer}. Should be either 1 or 2")
        return get_is_a_page()

    return answer == '2'

def get_name(element_type: str) -> str:
    return input(f"Enter {element_type}'s name : ")

def create_file(file_type, file_path, replace_values : list[Tuple[str, str]] = [], **formats) -> None:
    with open(f"./create_script/template.{file_type}", 'r') as template_file:
        new_file_content = template_file.read().format(**formats)

        # .format() has problems with the '{' and '}' characters they have to be
        # added here
        for old_str, new_str in replace_values:
            new_file_content = new_file_content.replace(old_str, new_str)

        with open(file_path, 'w') as new_file:
            new_file.write(new_file_content)

def create_files(*, is_a_page : bool, name : str) -> None:
    files_path : dict[str, str] = {
        "html": f"./templates/pages/{name}.html",
        "css": f"./static/css/pages/{name}.css",
        "js": f"./static/js/pages/{name}.js",
        "py": f"./scripts/{name}.py"
    }

    action_return : str = "''"
    if is_a_page:

        create_file("css", files_path["css"])
        create_file("js", files_path["js"])
        create_file("html", files_path["html"],
                    replace_values=[("% ", "{% "), (" %", " %}"), ('[', "{{"), (']', "}}")], name=name)
        action_return = f"render_template('/pages/{name}.html')"

    create_file("py", files_path["py"], name=name, is_a_page=is_a_page,
                class_name=name.replace(' ', ''), action_return=action_return)

def main() -> None:
    is_a_page : bool = get_is_a_page()
    element_type : str = "page" if is_a_page else "script"
    
    name : str = get_name(element_type)
    create_files(is_a_page=is_a_page, name=name)

if __name__ == "__main__":
    main()
