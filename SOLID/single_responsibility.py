"""The single responsibility principle (SRP) is a software design principle that states that every module, class, or function should have only one reason to change.
This means that each unit of code should be responsible for a single, well-defined task.
The SRP is important for several reasons.
First, it makes code easier to understand and maintain.
When each unit of code has a single responsibility, it is easier to see what that unit does and why it might need to change.
Second, the SRP can help to improve code cohesion. Cohesion is a measure of how well-related the different parts of a module are.
When each module has a single responsibility, the different parts of the module are more likely to be related to each other. This can make the code easier to read and understand.
Finally, the SRP can help to reduce coupling. Coupling is a measure of how tightly two modules are connected.
When two modules are tightly coupled, they are more likely to affect each other when they are changed.
This can make it difficult to change one module without affecting the other.
By following the SRP, you can help to reduce coupling between modules, which can make your code more flexible and easier to change.
Here is an example of the SRP. Let's say you have a class called FormatData.
This class preparing the data to writing into a csv file
From other side, there is class ExportCsv, which writes prepared data directly into 'out.csv'
By following the SRP, you can create code that is easier to understand, maintain, and change."""


class FormatData:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def prepare(self):
        result = ''
        for item in self.raw_data:
            new_line = ','.join((
                item['name'],
                item['surname'],
                item['occupation']
            )
            )
            result += f"{new_line}\n"
        return result


class ExportCsv:
    def __init__(self, filename):
        self.file = filename

    def write_file(self, current_data):
        with open(self.file, 'w', encoding='UTF-8') as f:
            f.write(current_data)


data = [
    {
        'name': 'Sherlock',
        'surname': 'Holmes',
        'occupation': 'private detective'
    },
    {
        'name': 'John',
        'surname': 'Watson',
        'occupation': 'doctor'
    }
]

formatter = FormatData(data)
formatted_data = formatter.prepare()
exporter = ExportCsv('out.csv')
exporter.write_file(formatted_data)
