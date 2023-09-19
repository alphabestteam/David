import datetime


def get_end_date(start_date, curr_assignments):
    sum_days = 0
    for work_days in curr_assignments:
        sum_days += work_days.work_days_amount
    return start_date + datetime.timedelta(days=sum_days)


def get_curr_cost(completed_assignments) -> float:
    sum_cost = 0
    for cost in completed_assignments:
        sum_cost += cost.salary
    return sum_cost


class Project:
    def __init__(self, project_desc: str, developers: list, all_assignments: list, curr_assignments, completed_assignments):
        self._project_desc = project_desc
        self._developers = developers
        self._all_assignments = all_assignments
        self._curr_assignments = curr_assignments
        self._completed_assignments = completed_assignments
        self._start_date = datetime.datetime.now()
        self._end_date = get_end_date(self.start_date, curr_assignments)
        self._curr_costs = get_curr_cost(completed_assignments)
        self._finished = False

    @property
    def developers(self):
        return self._developers

    @developers.setter
    def developers(self, value):
        self._developers = value

    @property
    def curr_costs(self):
        return self._curr_costs

    @curr_costs.setter
    def curr_costs(self, value):
        self._curr_costs = value

    @property
    def curr_assignments(self):
        return self._curr_assignments

    @curr_assignments.setter
    def curr_assignments(self, value):
        self._curr_assignments = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    @property
    def completed_assignments(self):
        return self._completed_assignments

    @completed_assignments.setter
    def completed_assignments(self, value):
        self._completed_assignments = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def all_assignments(self):
        return self._all_assignments

    @all_assignments.setter
    def all_assignments(self, value):
        self._all_assignments = value

    @property
    def finished(self):
        return self._finished

    @finished.setter
    def finished(self, value):
        self._finished = value

    @property
    def project_desc(self):
        return self._project_desc

    @project_desc.setter
    def project_desc(self, value):
        self._project_desc = value

    def add_assignment(self, assignment):
        if assignment not in self.all_assignments and assignment not in self.curr_assignments:
            if assignment.assignment_desc in [assignment.assignment_desc for assignment in self.curr_assignments]:
                raise "Project with the same description already exists"

            self.curr_assignments.append(assignment)
            self.all_assignments.append(assignment)
            self.end_date = get_end_date(
                self.start_date, self.curr_assignments)

        else:
            return "Assignment already in project"

    def remove_assignment(self, assignment):
        try:
            del self.curr_assignments[assignment]
            del self.curr_assignments[assignment]
            for dev in self.developers:
                if assignment in dev.curr_assignments:
                    del dev
        except AttributeError as error:
            return error
        self.end_date = get_end_date(self.start_date, self.curr_assignments)

    def search_assignment(self, assignment_desc):
        for assignment in self.all_assignments:
            if assignment_desc == assignment["desc"]:
                return assignment
            else:
                raise "assignment doesnt exist in this project"
