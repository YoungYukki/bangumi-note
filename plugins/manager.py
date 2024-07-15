import re
import shutil
import os


class Manager:
    def __init__(self) -> None:
        self.read()
        self.select_func()

    def select_func(self):
        func = input('1.选择\n2.添加\n3.删除\n执行功能:')
        match func:
            case '1': self.select_bangumi()
            case '2': self.add_func()
            case '3': self.remove_func()
            case _: exit()

    def add_func(self):
        added_bangumi = input('添加的番剧:')
        if added_bangumi:
            self.add(added_bangumi)
            self.add_func()
        else:
            self.select_func()

    def remove_func(self):
        removed_bangumi = input('删除的番剧:')
        if removed_bangumi:
            self.remove(removed_bangumi)
            self.remove_func()
        else:
            self.select_func()

    def select_bangumi(self):
        number = 0
        for bangumi in self.bangumi_list:
            print(f'{number}.{bangumi}\t')
            number += 1
        selected_ID = input('选择番剧:')
        if selected_ID:
            self.bangumi = self.bangumi_list[int(selected_ID)]
        else:
            exit()

    def read(self):
        with open('README.md', 'r', encoding='utf-8') as f:
            text = f.read()
        pattern = re.compile(r'(?<=\+\s\[).+(?=\])')
        self.bangumi_list = pattern.findall(text)
        print(self.bangumi_list)

    def add(self, bangumi: str):
        self.bangumi_list.append(bangumi.replace(' ', ''))
        self.commit()

    def remove(self, bangumi: str):
        if not bangumi in self.bangumi_list:
            print('不存在')
            return None
        self.bangumi_list.remove(bangumi)
        note_path = os.path.join('note', bangumi)
        if os.path.exists(note_path):
            shutil.rmtree(note_path)
        self.commit()

    def commit(self):
        bangumi_list = [
            f'+ [{bangumi}](note/{bangumi}/main.md)'
            for bangumi in self.bangumi_list
        ]
        text = '# 目录\n'
        text += '\n'.join(bangumi_list)
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(text)
