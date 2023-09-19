class Developer:
    def __init__(self, name, completed_assignments, curr_assignments, total_work_days, salary_sum):
        self._name = name
        self._completed_assignments = completed_assignments
        self._curr_assignments = curr_assignments
        self._total_work_days = total_work_days
        self._salary_sum = salary_sum
        self._work_years = 1

    def complete_assignment(self, assignment, project):
        if assignment.assigned_developer is self:

            assignment.finished = True
            self.work_years += assignment.assignment_complexity
            self.salary_sum += assignment.salary

            took_time = assignment.end_date - assignment.start_date
            self.total_work_days += took_time.days
            self.completed_assignments.append(assignment)

            project.completed_assignments.append(assignment)
        else:
            raise "Cant complete an assignment you weren't assigned too"

    @property
    def curr_assignments(self):
        return self._curr_assignments

    @curr_assignments.setter
    def curr_assignments(self, value):
        self._curr_assignments = value

    @property
    def total_work_days(self):
        return self._total_work_days

    @total_work_days.setter
    def total_work_days(self, value):
        self._total_work_days = value

    @property
    def salary_sum(self):
        return self._salary_sum

    @salary_sum.setter
    def salary_sum(self, value):
        self._salary_sum = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def work_years(self):
        return self._work_years

    @work_years.setter
    def work_years(self, value):
        self._work_years = value

    @property
    def completed_assignments(self):
        return self._completed_assignments

    @completed_assignments.setter
    def completed_assignments(self, value):
        self._completed_assignments = value
