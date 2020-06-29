import pytest
from WPR.AddVendorAccount_test import AddVendorAccount_test
from WPR.DepartmentTransferTest import department_transfer_test
from WPR.DailyMetric_test import DailyMetric_test
from WPR.TransferSiteTest import transferSite_test
from WPR.DBConnector import DBConnector_test


class Test_spec():

    #@pytest.mark.p2
    def test_fileVendorAccount(self):
        global driver
        global vendorName
        global accountName
        global updatedSiteOfCare
        global updatedAccountName
        vendorName = "Baxter"
        accountName = "TestVenMar91"
        updatedSiteOfCare = "Physician Clinic"
        updatedAccountName = "WAC"
        AddVendorAccount_test.test_setup(self)

        # To add vendor account
        AddVendorAccount_test.test_addVendor(self)
        print("Add Vendor Assertion")
        # To verify Added Account
        assert True == AddVendorAccount_test.test_VerifyAddedAccount(self, accountName)

        # To edit Vendor Account
        AddVendorAccount_test.test_EditVendor(self)
        print("Edit Vendor Assertion")
        # To verify Edited Account
        assert AddVendorAccount_test.test_verifyEditedAccount(self, accountName) == updatedAccountName

        # To delete vendor account
        AddVendorAccount_test.test_DeleteVendor(self)
        print("Delete Vendor Assertion")
        print(AddVendorAccount_test.test_verifyDeleteAccount(self, accountName))
        # To Verify Deleted Account
        assert False == AddVendorAccount_test.test_verifyDeleteAccount(self, accountName)

        AddVendorAccount_test.test_closeWindow(self)


    #@pytest.mark.p2
    def test_DepartmentTransfer(self):
        global warning_message;
        warning_message = 'Another active TransferDepartment is found with same Department Name'
        department_transfer_test.Enviornment(self)
        department_transfer_test.Data_Transfer_Depart(self)
        assert department_transfer_test.verifyDeptNameInDatabase(self) != 0
        department_transfer_test.Edit_Transfer_Site(self)
        assert department_transfer_test.Verify_Dupulicate_values(self) == warning_message
        department_transfer_test.test_closeWindow(self)

    #@pytest.mark.p2
    def test_SiteTransfer(self):
        transferSite_test.Enviornment(self)
        transferSite_test.addTransferSiteManual(self)
        assert transferSite_test.verifySiteInDatabase(self) != 0
        transferSite_test.test_closeWindow(self)

    #@pytest.mark.p2
    def test_FetchRecored(self):
        #assert DBConnector_test.fetchDepartment(self,"e2e47034") != 0
        assert DBConnector_test.fetchSite(self,"e2e70154") != 0

    @pytest.mark.p2
    def test_dailyMetric(self):
            global driver
            global primaryMetric
            global secondaryMetric
            #primaryMetric = "CMI Total Hospital - CMI"
            primaryMetric = "Patient Days (actual - excluding newborns) - PD"
            secondaryMetric = "CMI Total Hospital - CMI"
            DailyMetric_test.test_setup(self)
            DailyMetric_test.test_primaryMetric(self)
            DailyMetric_test.test_secondaryMetric(self)
            assert DailyMetric_test.test_verifyPrimaryMetric(self) == primaryMetric
            assert DailyMetric_test.test_verifySecondaryMetric(self) == secondaryMetric
            DailyMetric_test.test_primaryMetricReset(self)
            DailyMetric_test.test_secondaryMetricReset(self)

            '''DailyMetric_test.test_verifyCustomizePrimaryDescrption(self)
            assert True == DailyMetric_test.test_verifyAdjustPrimaryMetric(self)
            assert True == DailyMetric_test.test_verifyPrimaryWithCarveout(self)
            
            assert True == DailyMetric_test.test_verifyAdjustSecondaryMetric(self)
            assert True == DailyMetric_test.test_verifysecondaryWithCarveout(self)
            DailyMetric_test.test_closeWindow(self)'''