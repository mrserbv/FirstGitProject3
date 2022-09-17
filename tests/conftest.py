import pytest

cnt = 0

@pytest.fixture(autouse=True)
def clean_text_file():
    global cnt
    with open("testfile.txt", "w") as file:
        pass
    print(cnt)
    cnt +=1