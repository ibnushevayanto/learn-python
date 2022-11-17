with open("./Input/Letters/starting_letter.txt", mode="r") as file_starting_letter:

    isiSurat = file_starting_letter.read()
    print(isiSurat)
    with open("./Input/Names/invited_names.txt", mode="r") as file_penerima:

        listPenerima = file_penerima.readlines()
        for penerima in listPenerima:

            isiSuratEdited = isiSurat.replace("[name]", penerima.strip())
            with open(f"./Output/ReadyToSend/letter_for_{penerima.strip()}.txt", mode="w") as file:

                file.write(isiSuratEdited)
