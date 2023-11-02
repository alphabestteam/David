const studentConstructor = (name, age, grades) => {
    return {
        name: name,
        age: age,
        grades: grades,
        avgGrade: function () {
            let sum = this.grades.reduce((sum, value) => sum + value)
            let totalVowels = this.name.split("").map(char => "aeiouAEIOU".includes(char)).length
            let average = sum / this.grades.length + totalVowels
            return average.toFixed(2)
        }
    }
}

const carConstructor = (brand, model, year) => {
    return {
        brand: brand,
        model: model,
        year: year,
        age: function () {
            const date = new Date()
            return date.getFullYear() - this.year
        }
    }
}

function getStudentsInfo(student) {
    return `name: ${student.name} \nage: ${student.age} \ngrades: ${student.grades} \navgGrade: ${student.avgGrade()}\n`
}

function getCarInfo(car) {
    return `brand: ${car.brand} \nmodel: ${car.model} \nyear: ${car.year} \nage: ${car.age()}\n`

}

const student1 = studentConstructor("Dovid", 21, [100, 100, 100])
const student2 = studentConstructor("Biden", 1000, [50, 50, 25])
const student3 = studentConstructor("Trump", 75, [100, 100, 100])
const student4 = studentConstructor("Obama", 65, [80, 40, 80])
const student5 = studentConstructor("GoodOlGorge", 130, [80, 80, 80])

const students = [student1, student2, student3, student4, student5]

for (let i = 0; i < students.length; i++) {
    console.log(`students index ${i}`)
    console.log(getStudentsInfo(students[i]))
}

const adults = students.filter(student => student.age > 18)
console.log(adults)


const car = carConstructor("Audi", "A8", 2015)
console.log(getCarInfo(car))
