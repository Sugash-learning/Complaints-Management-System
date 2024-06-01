class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def file_complaint(self, system, description):
        system.file_complaint(self, description)


class Complaint:
    def __init__(self, complaint_id, user, description):
        self.complaint_id = complaint_id
        self.user = user
        self.description = description
        self.status = 'Pending'

    def __str__(self):
        return f'Complaint ID: {self.complaint_id}, User: {self.user.name}, Description: {self.description}, Status: {self.status}'


class Admin:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name

    def view_complaints(self, system):
        for complaint in system.complaints:
            print(complaint)

    def resolve_complaint(self, system, complaint_id):
        for complaint in system.complaints:
            if complaint.complaint_id == complaint_id:
                complaint.status = 'Resolved'
                return f'Complaint ID {complaint_id} resolved.'
        return f'Complaint ID {complaint_id} not found.'


class ComplaintSystem:
    def __init__(self):
        self.users = []
        self.admins = []
        self.complaints = []
        self.next_complaint_id = 1

    def register_user(self, user_id, name):
        user = User(user_id, name)
        self.users.append(user)
        return user

    def register_admin(self, admin_id, name):
        admin = Admin(admin_id, name)
        self.admins.append(admin)
        return admin

    def file_complaint(self, user, description):
        complaint = Complaint(self.next_complaint_id, user, description)
        self.complaints.append(complaint)
        self.next_complaint_id += 1
        return complaint

    def view_complaints(self):
        for complaint in self.complaints:
            print(complaint)

    def resolve_complaint(self, complaint_id):
        for complaint in self.complaints:
            if complaint.complaint_id == complaint_id:
                complaint.status = 'Resolved'
                return f'Complaint ID {complaint_id} resolved.'
        return f'Complaint ID {complaint_id} not found.'


# Create Complaint System
system = ComplaintSystem()

# Register Users
user1 = system.register_user(1, 'Sugash')
user2 = system.register_user(2, 'Dinesh')

# Register Admin
admin = system.register_admin(1, 'Admin1')

# Users file complaints
user1.file_complaint(system, 'Issue with the billing system.')
user2.file_complaint(system, 'Unable to login to the portal.')

# Admin views complaints
print("Complaints:")
admin.view_complaints(system)

# Admin resolves a complaint
print("\nResolving a complaint:")
print(admin.resolve_complaint(system, 1))

# View complaints after resolution
print("\nComplaints after resolution:")
admin.view_complaints(system)