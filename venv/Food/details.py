
from DBConnection import DBConnection

class Details:

    @staticmethod
    def getCal(fname):
        
        database = DBConnection.getConnection()
        cursor = database.cursor()
        cursor.execute("select calorie from dataset where fname='"+fname+"' ")
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])
            cal=row[0]
        return cal

if __name__ == '__main__':
    print(Details.getCal('pancakes'))
