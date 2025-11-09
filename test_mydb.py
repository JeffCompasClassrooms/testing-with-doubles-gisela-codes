import pytest
import pickle

from mydb import MyDB


def describe_MyDB():

    def describe_init():
        def it_creates_file_when_missing(mocker):
            mocker.patch("os.path.isfile", return_value=False)
            mock_saveStrings = mocker.patch.object(MyDB, "saveStrings")

            db = MyDB("fakedb.db")

            # saveStrings was called once?
            mock_saveStrings.assert_called_once_with([])

        def it_does_not_overwrite_existing_file(mocker):
            mocker.patch("os.path.isfile", return_value=True)
            mock_saveStrings = mocker.patch.object(MyDB, "saveStrings")

            MyDB("fakedb.db")

            mock_saveStrings.assert_not_called()


    def describe_loadStrings():
        def it_returns_list_of_strings(mocker):
            lst = ["Chip", "Dale", "Sparky"]
            mock_open = mocker.patch("builtins.open", mocker.mock_open())
            mocker.patch("pickle.load", return_value=lst)

            db = MyDB("fake.pkl")

            result = db.loadStrings()
            assert result == lst
            
        def it_raises_error_for_non_pickle_file(mocker):
            mocker.patch("os.path.isfile", return_value=True)
            bad_data = b"not a pickle file"
            mock_open = mocker.mock_open(read_data=bad_data)
            mocker.patch("builtins.open", mock_open)

            db = MyDB("fake.pkl")
            
            with pytest.raises(pickle.UnpicklingError):
                db.loadStrings()
        

    def describe_saveStrings():
        def it_writes_list_to_file(mocker):
            pass
        def it_overwrites_previous_content(mocker):
            pass


    def describe_saveString():
        def it_creates_file_if_missing(mocker):
            pass
        def it_only_adds_strings(mocker):
            pass
        def it_appends_new_string_to_existing_list(mocker):
            pass