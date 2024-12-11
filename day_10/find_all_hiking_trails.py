import map_management

if __name__ == '__main__':
    map = map_management.get_python_list_from_input()
    trailheads = []
    hiking_trails = []
    for north_south_loc, latitude in enumerate(map):
        for east_west_loc, elevation in enumerate(latitude):
            if elevation == '0':
                trailheads.append([north_south_loc, east_west_loc]) 
    for trailhead in trailheads:
        trailhead_obj = map_management.trail_finder(trailhead)
        trailhead_obj.find_hiking_trail([trailhead])
        successful_trails = trailhead_obj.get_hiking_trails()
        hiking_trails += successful_trails
    print(len(hiking_trails))