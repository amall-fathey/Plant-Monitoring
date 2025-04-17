from .models import Plant
import os

def migrate_csv_file(file_name):
    row = 0
    try:
        # Read all data first
        with open(file_name, 'rb') as fle:
            lines = fle.read().decode().split('\r\n')
            
        # Remove empty lines
        lines = [line for line in lines if line.strip()]
        total = len(lines)
        for line in lines:
            try:
                data = line.split(';')[1::]
                if len(data) == 9:
                    Plant.objects.create(
                        Soil_Moisture=data[0],
                        Temperature=data[1],
                        Soil_Humidity=data[2],
                        Air_temperature=data[3],
                        Air_humidity=data[4],
                        Pressure=data[5],
                        ph=data[6],
                        Status=data[7],
                        rainfall=data[8]
                    )
                    row += 1
                    percentage = (row / total) * 100
                    print(f"{int(percentage)}% Done")

            except Exception as e:
                continue
        
        return f"Successfully processed {processed_count} records"
    
    except Exception as e:
        return f"Failed to process file: {str(e)}"

if __name__ == "__main__":
    result = migrate_csv_file(".\Dataa.csv")
    print(result)