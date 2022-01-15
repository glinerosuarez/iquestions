from algos.island_perimeter.island_perimeter import Solution


def test_island_perimeter():
    assert Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
    assert Solution().islandPerimeter([[1,1,1],[1,0,1]]) == 12

    
if __name__ == '__main__':
    test_island_perimeter()