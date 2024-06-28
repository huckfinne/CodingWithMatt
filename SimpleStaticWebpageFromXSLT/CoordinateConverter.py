import csv
from OSGridConverter import grid2latlong


def convert_csv_coordinates(input_csv_path, output_csv_path):
    with open(input_csv_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        with open(output_csv_path, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            csv_writer.writerow(header + ['latitude', 'longitude'])

            for row in csv_reader:
                grid_ref = row[3]

                if grid_ref == '':
                    continue

                try:
                    l = grid2latlong(grid_ref, tag='WGS84')
                    csv_writer.writerow(row + [l.latitude, l.longitude])
                except ValueError as e:
                    print(f"Error parsing grid reference {grid_ref}: {e}")
