import os

# file paths
inDir = "."
ending = ".sav"
outDir = "clear_known_memory"

# known memory
# [pos, len],
known_memory = [
    # Character Name
    [0x6314, 12], [0x6714, 12], [0x6B14, 12], [0x6F14, 12],

    # My Decks (4x) Autosave
    [0x200, 0x54 * 4],
    # My Decks (4x) Diary
    [0x4200, 0x54 * 4],
    # Deck Machine (60x) Autosave
    [0x350, 0x54 * 60],
    # Deck Machine (60x) Diary
    [0x4350, 0x54 * 60],

    # just time runnig, no changes -> clock?
    [0x1804, 1], [0x180A, 3], [0x191E, 1],
    [0x5804, 1], [0x580A, 3], [0x591E, 1]
]

for inFilePath in os.listdir(inDir):
    if inFilePath.endswith(ending):

        # read file
        with open(inFilePath, "rb") as file:
            data = bytearray(file.read())
        
        # clear known memory
        for mem in known_memory:
            for i in range(mem[0], mem[0]+mem[1]):
                data[i] = 0x00
        
        # write file
        outFilePath = os.path.join(outDir, inFilePath)
        print(outFilePath)
        with open(outFilePath, "wb") as file:
            file.write(data)
