CREATE TABLE "Legacy_Roles" (ID COUNTER(10), Role VARCHAR(255), Block BIT(1), Role_Description VARCHAR(255), Stream VARCHAR(255));
CREATE TABLE "Legacy_Tcodes" (ID COUNTER(10), Role VARCHAR(255), Tcode VARCHAR(255), Tcode_Description VARCHAR(255));
CREATE TABLE "Legacy_User_Role" (User_Name VARCHAR(255), Role VARCHAR(255), Start_date DATETIME(19), End_date DATETIME(19), Active BIT(1));
CREATE TABLE "Legacy_Users" (ID COUNTER(10), User_Name VARCHAR(255), Full_Name VARCHAR(255), User_Master VARCHAR(255), Locked VARCHAR(255), Reason_User_Lock VARCHAR(255), Valid_from DATETIME(19), Valid_To DATETIME(19), Complete BIT(1), Exclude BIT(1));
CREATE TABLE "LegacyImport" (ID COUNTER(10), User_Name VARCHAR(255), Full_Name VARCHAR(255), Role VARCHAR(255), Assignment__Reference_User_ VARCHAR(255), Start_date DATETIME(19), End_date DATETIME(19), Short_Role_Description VARCHAR(255), Valid_from DATETIME(19), Valid_To DATETIME(19), User_Master_Maintenance__User_Group VARCHAR(255), Locked VARCHAR(255), Reason_for_User_Lock VARCHAR(255));
CREATE TABLE "Questions" (ID COUNTER(10), Question VARCHAR(255), Answered BIT(1));
CREATE TABLE "S4_RoleDescriptions" (ID COUNTER(10), Application VARCHAR(255), E2E_stream VARCHAR(255), Sub_stream VARCHAR(255), Business_Role_Name VARCHAR(255), Description LONGCHAR(1073741823), Role_Description LONGCHAR(1073741823), Comments LONGCHAR(1073741823), Usage VARCHAR(255), AdditionalComments VARCHAR(255));
CREATE TABLE "S4_Roles" (E2E_stream VARCHAR(255), Sub_stream VARCHAR(255), Business_Role_Name VARCHAR(255), Description VARCHAR(255));
CREATE TABLE "S4_Roles_Tcodes" (ID COUNTER(10), Application VARCHAR(255), E2E_stream VARCHAR(255), Sub_stream VARCHAR(255), Business_Role_Name VARCHAR(255), Tcode_App VARCHAR(255), Description VARCHAR(255), Global_Composite_Role_Name VARCHAR(255), Template_Role VARCHAR(255), Template_Role_Name VARCHAR(255));
CREATE TABLE "S4_Tcodes" (ID COUNTER(10), Application VARCHAR(255), E2E_stream VARCHAR(255), Sub_stream VARCHAR(255), Business_Role_Name VARCHAR(255), Tcode VARCHAR(255), Description VARCHAR(255), Global_Composite_Role_Name VARCHAR(255), Template_Role VARCHAR(255), Template_Role_Name VARCHAR(255));
CREATE TABLE "S4_User_Role" (User_Name VARCHAR(255), Role VARCHAR(255), E2E_stream VARCHAR(255));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE users (
    "ID" COUNTER(10),
    "username" TEXT,
    "email" TEXT,
    "name" TEXT,
    "pwd" TEXT,
    "force" TEXT
);
