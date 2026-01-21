<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

# This is the document folder for me and my team's assignment in Database Systems
This assignment is focused on designing and implementing a Relational Database for **Topic 6: Hotel Management (Khách sạn – Phòng – Khách – Đặt phòng)** using PostgreSQL.

# Table of Contents:
1. [Team Members](#team-member)
2. [Work Plan](#work-plan)
    1. [Phase 1](#phase-one)
    2. [Phase 2](#phase-two)
    3. [Phase 3](#phase-three)
    4. [Phase 4](#phase-four)
3. [Notes](#notes)
4. [Documents](#documents)

## Our team <a id = "team-member"></a>

<div align="center">
    <table>
        <tr>
        <th>Student Id</th> 
        <th>Full Name</th> 
        <th>Role</th>
        </tr>
        <tr>
            <td>24521421</td> 
            <td>Vũ Minh Phương</td>
            <td>Data Engineering, Querying & Security</td>
        </tr>
        <tr>
            <td>24520041</td>
            <td>Đào Đình An</td>
            <td>Database Structure, Algebra & System Logic</td>
        </tr>
    </table>
</div>

## Work Plan (Timeline: 3 Days): <a id = "work-plan"></a>

The project is divided into 4 Logical Phases:

### Phase 1: Infrastructure Initialization (DDL) <a id = "phase-one"></a>
**Focus:** Establishing the database schema and handling circular references.
- **DDL Design:** Write `CREATE TABLE` scripts for `PHONG`, `KHACH`, `DATPHONG`.
- **Constraint Handling:** Define Primary Keys (PK) and standard data types.
- **Mutual Foreign Keys:** Solve the "Chicken & Egg" problem between `PHONG` and `DATPHONG` using `ALTER TABLE` strategies.

### Phase 2: Data Engineering (DML) <a id = "phase-two"></a>
**Focus:** Generating meaningful seed data for complex querying.
- **Data Scenarios:** Prepare logical datasets to satisfy "Division Query" (The guest who booked all rooms) and "Trigger Violation" cases.
- **Insertion Strategy:** 
    - Insert `KHACH`.
    - Insert `PHONG` (with NULL FK).
    - Insert `DATPHONG`.
    - Update `PHONG` to fill circular FKs.
- **Volume Goal:** Ensure 40-50 records per table.

### Phase 3: Query Processing & Views <a id = "phase-three"></a>
**Focus:** Solving business questions using Relational Algebra and SQL.
- **Relational Algebra:** Write formal expressions for specific queries (Selection, Projection, Join).
- **Basic SQL & Views:** Implement statistical queries and create 3 required Views.
- **Advanced SQL:** Implement the "Division Query" (finding guests who booked all room types that a specific guest booked) using `NOT EXISTS` or `HAVING` clauses.

### Phase 4: Advanced Logic, Security & Reporting <a id = "phase-four"></a>
**Focus:** Ensuring data integrity and packaging the project.
- **Triggers (PL/pgSQL):** 
    - Disable declarative constraints.
    - Implement Logic: Check Dates (`NgayTra >= NgayNhan`), Consistency (`MaDatHienTai`), and Referential Integrity (`DELETE` protection).
- **Security:** Implement `GRANT/REVOKE` scenarios for users A, B, C, D, E and analyze the Cascade effects.
- **Reporting:** Compile all SQL Scripts and write the final documentation (DOCS).

## Notes: <a id = "notes"></a>
- **DBMS:** PostgreSQL.
- **Critical Requirement:** Must handle the Circular Foreign Key between `PHONG` and `DATPHONG` correctly.
- **Submission Structure:** Folder `MSSV1_MSSV2` containing `SCRIPTS` and `DOCS`.

## Documents: <a id = "documents"></a>
Reference materials for the assignment.

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Relational Algebra Calculator](https://ratest.softagram.com/)
- [PL/pgSQL Trigger Tutorial](https://www.postgresqltutorial.com/postgresql-triggers/)
- [Database Systems Course Outline - UIT](https://www.uit.edu.vn)
