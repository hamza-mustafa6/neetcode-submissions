class Solution:
    from collections import deque
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ogColor = image[sr][sc]

        if ogColor == color:
            return image

        queue = deque()
        queue.append((sr,sc))
        image[sr][sc] = color
        rows = len(image)
        cols = len(image[0])
        
        while(queue):
            (r, c) = queue.popleft()
            image[r][c] = color
            if r-1 >= 0:
                if image[r-1][c] == ogColor:
                    queue.append((r-1,c))
                    image[r-1][c] == color
            if c-1 >= 0:
                if image[r][c-1] == ogColor:
                    queue.append((r,c-1))
                    image[r][c-1] == color
            if r+1 < rows:
                if image[r+1][c] == ogColor:
                    queue.append((r+1,c))
                    image[r+1][c] == color
            if c+1 < cols:
                if image[r][c+1] == ogColor:
                    queue.append((r,c+1))
                    image[r][c+1] == color

        return image
            


