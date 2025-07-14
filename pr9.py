import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self):
        self.df = None

    def load_dataset(self):
        path = input("Enter CSV file path: ")
        try:
            self.df = pd.read_csv(path)
            print("Dataset loaded successfully!")
        except FileNotFoundError:
            print("File not found.")
            self.df = None

    def explore_data(self):
        if self.df is None:
            print("Please load a dataset.")
            return

        while True:
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back to main menu")
            choice = input("Enter your choice: ")

            match choice:
                case '1':
                    print(self.df.head())
                case '2':
                    print(self.df.tail())
                case '3':
                    print(self.df.columns.tolist())
                case '4':
                    print(self.df.dtypes)
                case '5':
                    print(self.df.info())
                case '6':
                    break
                case _:
                    print("Invalid choice!")

    def dataframe_operations(self):
        if self.df is None:
            print("Please load a dataset first.")
            return
        
        print("1. Sort by Column")
        print("2. Filter Rows by Value")
        print("3. Display Unique Values of a Column")
        choice = input("Choose operation: ")

        match choice:
            case '1':
                column = input("Enter column to sort by: ")
                if column in self.df.columns:
                    print(self.df.sort_values(by=column))
                else:
                    print("Column not found.")
            case '2':
                column = input("Enter column to filter by: ")
                value = input("Enter value to filter: ")
                if column in self.df.columns:
                    print(self.df[self.df[column] == value])
                else:
                    print("Column not found.")
            case '3':
                column = input("Enter column to view unique values: ")
                if column in self.df.columns:
                    print(self.df[column].unique())
                else:
                    print("Column not found.")
            case _:
                print("Invalid operation.")

    def handle_missing_data(self):
        if self.df is None:
            print("Please load a dataset first.")
            return

        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        choice = input("Enter your choice: ")

        if self.df.isnull().sum().sum() == 0:
            print("No missing values.")
            return

        match choice:
            case '1':
                print(self.df[self.df.isnull().any(axis=1)])
            case '2':
                self.df.fillna(self.df.mean(numeric_only=True), inplace=True)
                print("Missing values filled.")
            case '3':
                self.df.dropna(inplace=True)
                print("Missing values dropped.")
            case '4':
                value = input("Enter the value to replace missing values with: ")
                self.df.fillna(value, inplace=True)
                print("Missing values replaced.")
            case _:
                print("Invalid choice.")

    def generate_statistics(self):
        if self.df is None:
            print("Please load a dataset.")
            return
        print(self.df.describe())

    def data_visualization(self):
        if self.df is None:
            print("Please load a dataset.")
            return
        
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie chart")
        print("5. Histogram")
        print("6. Stack Plot")
        choice = input("Enter your choice: ")

        x = input("Enter x-axis column name: ")
        y = input("Enter y-axis column name: ")

        match choice:
            case '1':
                self.df.plot.bar(x=x, y=y)
            case '2':
                self.df.plot.line(x=x, y=y)
            case '3':
                self.df.plot.scatter(x=x, y=y)
            case '4':
                self.df[y].value_counts().plot.pie(autopct='%1.1f%%')
            case '5':
                self.df[y].plot.hist()
            case '6':
                self.df[[x, y]].plot.area(stacked=True)
            case _:
                print("Invalid choice.")
                return

        plt.title(f"{x} vs {y}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def save_visualization(self):
        filename = input("Enter file name to save: ")
        try:
            plt.savefig(filename)
            print(f"{filename} saved successfully!")
        except Exception :
            print(Exception)

def main():
    analyzer = DataAnalyzer()

    while True:
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                analyzer.load_dataset()
            case '2':
                analyzer.explore_data()
            case '3':
                analyzer.dataframe_operations()
            case '4':
                analyzer.handle_missing_data()
            case '5':
                analyzer.generate_statistics()
            case '6':
                analyzer.data_visualization()
            case '7':
                analyzer.save_visualization()
            case '8':
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
