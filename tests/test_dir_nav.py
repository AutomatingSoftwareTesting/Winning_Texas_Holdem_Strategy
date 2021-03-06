from app.dir_nav import DirNav
setup_specific_path = "C:\\Users\\jdcald13\\Documents\\repos\\Winning_Texas_Holdem_Strategy\\"


class TestFolderNavigation:
    """These checks will be different for each implementation (setup)."""
    def test_folder_nav(self):
        image = DirNav()
        table = image.get_path("tables")
        assert table == setup_specific_path + "../images/tables/"

        image = DirNav()
        table = image.get_path("cards")
        assert table == setup_specific_path + "../images/cards/"

        image = DirNav()
        table = image.get_path("hand_ranges")
        assert table == setup_specific_path + "../hand_ranges/"

        image = DirNav()
        table = image.get_path("reports")
        assert table == setup_specific_path + "../reports/"

    def test_unknown_folder(self):
        image = DirNav()
        image = image.get_path("image")
        assert image == "Sorry, unknown folder."

    def test_full_name(self):
        file1 = DirNav("6_Handed_Table.png")
        file1.get_path("tables")
        assert str(file1) == setup_specific_path + "../images/tables/6_Handed_Table.png"

        file2 = DirNav("Kd.png")
        file2.get_path("cards")
        assert str(file2) == setup_specific_path + "../images/cards/Kd.png"

        file3 = DirNav("Unimproved Range.txt")
        file3.get_path("hand_ranges")
        assert str(file3) == setup_specific_path + "../hand_ranges/Unimproved Range.txt"

        file4 = DirNav("practice.csv")
        file4.get_path("reports")
        assert str(file4) == setup_specific_path + "../reports/practice.csv"
