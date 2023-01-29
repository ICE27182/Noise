

def gen_hash_table(seed=None):
    """Provide a hash table whose length is 512 and where numbers in range(255) are placed 
    in a random order and repeated once."""
    import random
    random.seed(seed)

    hash_table = []
    nums = list(range(256))
    for _ in range(256):
        index = random.randint(0,len(nums)-1)
        hash_table.append(nums[index])
        nums.pop(index)

    hash_table += hash_table    # Repeat once

    return tuple(hash_table)


def to_text(R=255,G=255,B=255):
    """Turn the chunks into a colorful long string to output."""
    def to_color(val):
        return f"\033[38;2;{int(R/255*val)};{int(G/255*val)};{int(B/255*val)}m██\033[0m"
    
    text_list = []
    for Y in range(chunks_size[1]-1, -1, -1):   # Every row of the chunks
        for y in range(chunk_width-1, -1, -1):  # Every row in a row of the chunks (Relative y)
            text_list.append("\n")
            for chunk in chunks[Y]:             # Every chunk in a row of chunks
                for x in range(chunk_width):    # (Relative x)
                    text_list.append(to_color(chunk.points[y][x]))
    
    return "".join(text_list)


class Chunk:
    def __init__(self,chunk_tag) -> None:
        """Set all four vertices' values and all points' values in the chunk."""
        if type(chunk_tag) not in (tuple,list):
            raise Exception("Chunk __init__ chunk_tag type error")
        if len(chunk_tag) != 2:
            raise Exception("Chunk __init__ chunk_tag length error")
        
        self.tag = (chunk_tag[0], chunk_tag[1])

        # The commented codes makes the image depends on the chunk_width, so chunk_width will no longer
        # represent the image resolution(or accuracy perhaps?), and instead, it will directly affect the image
        # itself, which may not be so ideal.

        # coor = (chunk_tag[0] * chunk_width, chunk_tag[1] * chunk_width)
        # self.lb = hash_table[hash_table[coor[0] % 256] + coor[1] % 256]
        # self.lt = hash_table[hash_table[coor[0] % 256] + (coor[1]+chunk_width) % 256]
        # self.rb = hash_table[hash_table[(coor[0]+chunk_width) % 256] + coor[1] % 256]
        # self.rt = hash_table[hash_table[(coor[0]+chunk_width) % 256] + (coor[1]+chunk_width) % 256]
        
        self.lb = hash_table[hash_table[chunk_tag[0] % 256] + chunk_tag[1] % 256]
        self.lt = hash_table[hash_table[chunk_tag[0] % 256] + (chunk_tag[1]+1) % 256]
        self.rb = hash_table[hash_table[(chunk_tag[0]+1) % 256] + chunk_tag[1] % 256]
        self.rt = hash_table[hash_table[(chunk_tag[0]+1) % 256] + (chunk_tag[1]+1) % 256]

        self.points = []
        Chunk.cal_points(self)
    

    def cal_points(self):
        '''Calculate all points' values in the chunk'''
        def fade(x):
            return 6*x**5-15*x**4+10*x**3
        
        for y in range(chunk_width):
            self.points.append([])
            for x in range(chunk_width):
                val = (
                    (
                    self.lb * fade(1 - x / chunk_width) +
                    self.rb * fade(x / chunk_width)
                    ) * fade(1 - y / chunk_width) +
                    (
                    self.lt * fade(1 - x / chunk_width) +
                    self.rt * fade(x / chunk_width)
                    ) * fade(y / chunk_width)
                )
                self.points[y].append(val)


    def gen_chunks():
        """Generate chunks according to chunk_width and chunks_size."""
        chunks = []
        for Y in range(chunks_size[1]):
            chunks.append([])
            for X in range(chunks_size[0]):
                chunks[Y].append(Chunk((X, Y)))
        return chunks



if __name__ == "__main__":
    seed = 0
    chunk_width = 16
    chunks_size = (4,4)
    cycle = False
    
    hash_table = gen_hash_table(seed)

    chunks = Chunk.gen_chunks()
    # print(to_text())    #Output a too string seems to meet a problem that some � will emerge
    output = tuple(to_text().split("\n"))
    for row in output:
        print(row)
    
    if cycle == True:
        from time import sleep
        while True:
            sleep(0.64)
            seed += 1
            hash_table = gen_hash_table(seed)

            chunks = Chunk.gen_chunks()

            output = tuple(to_text().split("\n"))
            for row in output:
                print(row)