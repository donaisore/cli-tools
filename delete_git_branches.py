import fire
import sys
import inquirer
import subprocess

def delete_git_branches():
    output = subprocess.check_output(['git', '-P', 'branch'])
    branch_list = output.decode().replace(' ', '').replace('*', '').split('\n')[:-1]

    questions = [inquirer.Checkbox(
        'delete_branch_list',
        message="削除するブランチを選択",
        choices=branch_list
    )]

    answers = inquirer.prompt(questions)

    if not answers:
        sys.exit()

    delete_branch_list = answers.get('delete_branch_list')

    if delete_branch_list:
        subprocess.call(['git', 'branch', '-D'] + delete_branch_list)
    print('選択されたブランチはありませんでした。')


if __name__ == '__main__':
    fire.Fire(delete_git_branches)
