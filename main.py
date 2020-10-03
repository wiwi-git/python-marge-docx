from docxcompose.composer import Composer
from docx import Document as Document_compose


def combine_all_docx(filename_master, files_list):
    number_of_sections = len(files_list)
    master = Document_compose(filename_master)
    composer = Composer(master)
    for i in range(0, number_of_sections):
        doc_temp = Document_compose(files_list[i])
        composer.append(doc_temp)
    composer.save("combined_file.docx")


if __name__ == '__main__':
    prefixName = 'IMG_0'
    suffixName = '.docx'

    startNumber = 222

    files = []

    for i in range(71):
        fileNumber = startNumber + i
        fileName = prefixName + str(fileNumber) + suffixName
        files.append(fileName)

    masterName = prefixName + str(startNumber - 1) + suffixName
    combine_all_docx(masterName, files)
