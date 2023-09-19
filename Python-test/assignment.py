import datetime


class Assignment:
    def __init__(self, assignment_desc, assigned_to_project, work_days_amount, assignment_complexity):
        self._assignment_desc = assignment_desc
        self._assigned_to_project = assigned_to_project
        self._work_days_amount = work_days_amount
        self._assignment_complexity = assignment_complexity
        self._assigned_developer = None
        self._start_date = datetime.datetime.now()
        self._end_date = self.start_date + datetime.timedelta(days=10)

        self._salary = 0
        self._finished = False

    def assign_developer(self, developer, project):
        for assignments in developer.curr_assignments:
            if assignments.assignment_desc == self.assignment_desc:
                raise "This developer already has an assignment with the same description"
        developer.curr_assignments.append(self)
        self.assigned_developer = developer
        self.salary = self.assigned_developer.work_years * \
            (self.assignment_complexity / self.work_days_amount)

        project.curr_assignments.append(self)

    @property
    def assignment_desc(self):
        return self._assignment_desc

    @assignment_desc.setter
    def assignment_desc(self, value):
        self._assignment_desc = value

    @property
    def assigned_to_project(self):
        return self._assigned_to_project

    @assigned_to_project.setter
    def assigned_to_project(self, value):
        self._assigned_to_project = value

    @property
    def work_days_amount(self):
        return self._work_days_amount

    @work_days_amount.setter
    def work_days_amount(self, value):
        self._work_days_amount = value

    @property
    def assigned_developer(self):
        return self._assigned_developer

    @assigned_developer.setter
    def assigned_developer(self, value):
        self._assigned_developer = value

    @property
    def assignment_complexity(self):
        return self._assignment_complexity

    @assignment_complexity.setter
    def assignment_complexity(self, value):
        self._assignment_complexity = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def finished(self):
        return self._finished

    @finished.setter
    def finished(self, value):
        self._finished = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
