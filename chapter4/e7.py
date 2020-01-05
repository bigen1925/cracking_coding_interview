import unittest
from copy import copy
from typing import List

from .Graph import Graph


class GraphE7(Graph):
    @classmethod
    def get_ordered_projects(
        cls, projects: List[str], dependencies: List[List[str]]
    ) -> List[str]:
        """
        実行可能順に並び替えたプロジェクトのリストを返す
        """

        are_done = {project: False for project in projects}
        ordered_projects = []

        # 依存関係を持つプロジェクトのdictを取得
        dependent_projects = {project: False for project in projects}
        for dependence in dependencies:
            dependent_projects[dependence[1]] = True

        # 依存関係を持たないプロジェクトをdoneとする
        for project in [
            project
            for project, is_dependent in dependent_projects.items()
            if is_dependent is False
        ]:
            are_done[project] = True
            ordered_projects.append(project)

        # 全てのプロジェクトがdoneになるまで、繰り返す
        while len(ordered_projects) < len(projects):
            # undoneなプロジェクトのうち、依存関係が全て満たされているものをdoneにする
            done_projects_exists = False
            for project in [
                project for project, is_done in are_done.items() if is_done is False
            ]:
                # 依存関係にあるプロジェクトでundoneのものがなければ、doneとする
                if not [
                    dependence
                    for dependence in dependencies
                    if dependence[1] == project and are_done[dependence[0]] is False
                ]:
                    done_projects_exists = True
                    are_done[project] = True
                    ordered_projects.append(project)

            # 1ループでdoneにできるプロジェクトがなくなったら、例外を送出する
            if not done_projects_exists:
                raise ValueError("依存関係を満たすプロジェクトの実行順が存在しません")

        return ordered_projects


class Test(unittest.TestCase):
    def test_it(self):
        projects = ["a", "b", "c", "d", "e", "f"]
        dependencies = [["a", "d"], ["f", "b"], ["b", "d"], ["f", "a"], ["d", "c"]]
        order = GraphE7.get_ordered_projects(projects, dependencies)

        self.check_dependencies(order, dependencies)

    @staticmethod
    def check_dependencies(projects: List[str], dependencies: List[List[str]]):
        for dependence in dependencies:
            before = projects.index(dependence[0])
            after = projects.index(dependence[1])
            assert before < after


if __name__ == "__main__":
    unittest.main()
