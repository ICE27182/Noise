

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
        self.chunk_tag = chunk_tag
        self.points = []
        Chunk.cal_points(self)
        

    def cal_points(self):
        '''Calculate all points' values in the chunk'''
        from math import sqrt
        def fade(x):
            return 6*x**5-15*x**4+10*x**3
        def hash(x,y):
            return hash_table[hash_table[x % 256] + y % 256]
        def gredient_dot(opt,coor_x,coor_y):
            if opt == 0:
                return  (coor_x-x) + (coor_y-y)
            elif opt == 1:
                return  (coor_x-x) - (coor_y-y)
            elif opt == 2:
                return -(coor_x-x) + (coor_y-y)
            elif opt == 3:
                return -(coor_x-x) - (coor_y-y)
            
        # Four gredient vectors (1,-1)(-1,1)(1,1)(-1,-1)
        # Four cases, so dot production can simply be addition and substraction without mutiplication
        lb = hash(self.chunk_tag[0],self.chunk_tag[1]) % 4
        lt = hash(self.chunk_tag[0],self.chunk_tag[1]+1) % 4
        rb = hash(self.chunk_tag[0]+1,self.chunk_tag[1]) % 4
        rt = hash(self.chunk_tag[0]+1,self.chunk_tag[1]+1) % 4

        for y in range(chunk_width):
            y /= chunk_width
            self.points.append([])
            for x in range(chunk_width):
                x /= chunk_width

                plb = gredient_dot(lb,0,0)
                plt = gredient_dot(lt,0,1)
                prb = gredient_dot(rb,1,0)
                prt = gredient_dot(rt,1,1)

                val = (
                        (
                            (
                                plb * fade(1 - x) +
                                prb * fade(x)
                            ) * fade(1 - y) 
                            +
                            (
                                plt * fade(1 - x) +
                                prt * fade(x)
                            ) * fade(y)
                        ) / sqrt(2) +1
                ) / 2 * 255
                self.points[int(y*chunk_width)].append(val)


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