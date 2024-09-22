db = db.getSiblingDB("mydb");

db.createCollection('users');

db.users.insertMany([
  { name: "John Doe", email: "john@example.com", age: 30 },
  { name: "Jane Smith", email: "jane@example.com", age: 25 },
  { name: "Michael Brown", email: "michael@example.com", age: 35 }
]);

print("User data inserted successfully");