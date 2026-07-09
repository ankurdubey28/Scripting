import os,shutil
from collections import defaultdict
from pathlib import Path
import typer

app=typer.Typer()


@app.command()
def sort(folder_path:str,dst:str)->None:
    files=os.listdir(folder_path)

    # traverse each file , find what is its 'type' and then put that into its own bucket
    buckets=defaultdict(list[str])

    for file in files:
        split_file=file.split(".")
        file_type=split_file[-1]

        if split_file[0]=="" or os.path.isdir(os.path.join(folder_path, file)):
            continue

        buckets[file_type].append(file)
        print(buckets)


    # now create folder for each of bucket type and dump files of container within that folder

    for folder,file in buckets.items():
        file.sort()

        directory=Path(f"{dst}{"/"}{folder}")
        directory.mkdir(0o777,parents=True,exist_ok=True)
        print(directory)

        for f in file:
            shutil.copy(os.path.join(folder_path,f), directory)



if __name__=="__main__":
    app()