def moveDiskByRecursion(disks):
    n = len(disks)
    
    positions = {
        'A': disks.copy(),
        'B': [],
        'C': []
    }

    moves = []

    def is_valid_move(disk, destination):
        if not destination:
            return True
        top_disk = destination[-1]
        return disk[0] < top_disk[0] and disk[1] != top_disk[1]

    def move_disk(from_rod, to_rod):
        disk = positions[from_rod][-1]
        if not is_valid_move(disk, positions[to_rod]):
            return False
        positions[from_rod].pop()
        positions[to_rod].append(disk)
        moves.append((disk[0], from_rod, to_rod))
        return True

    def verification(n, source, target, auxiliary):
        if n == 0:
            return True

        if not verification(n - 1, source, auxiliary, target):
            return False

        if not move_disk(source, target):
            return False

        if not verification(n - 1, auxiliary, target, source):
            return False

        return True

    success = verification(n, 'A', 'C', 'B')

    return moves if success else -1
