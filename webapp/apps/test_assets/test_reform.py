reform_text = """// Title: 2016 Trump Campaign Tax Plan
// Reform_File_Author: Matt Jensen
// Reform_Reference: https://www.donaldjtrump.com/policies/tax-plan
// Reform_Description:
// -  New personal income tax schedule (regular/non-AMT/non-pass-through) (1)
// -  New pass-through income tax schedule (2)
// -  New long-term capital gains and qualified dividends tax schedule (3)
// -  Repeal Alternative Minimum Tax (4)
// -  Repeal Net Investment Income Tax (5)
// -  Raise the Standard Deduction (6)
// -  Repeal the Personal Exemption (7)
// -  New above the line deduction for child and elder care (8)
// -  Cap itemized deductions (9)
// Reform_Parameter_Map:
// - 1: _II_rt*, II_brk*
// - 2: _PT_*
// - 3: _CG_*
// - 4: _AMT_*
// - 5: _NIIT_rt
// - 6: _STD
// - 7: _II_em
// - 8: _ALD_Dependents*
// - 9: _ID_c
{
    "policy": {
        "_II_rt1": {
            "2017": [0.12],
            "2018": [0.12]
        },
        "_II_brk1":
            {"2017": [[37500, 75000, 37500, 37500, 75000]]},
        "_II_rt2":
            {"2017": [0.25]},
        "_II_brk2":
            {"2017": [[112500, 225000, 112500, 112500, 225000]]},
        "_II_rt3":
            {"2017":  [0.25]},
        "_II_brk3":
            {"2017": [[112500, 225000, 112500, 112500, 225000]]},
        "_II_rt4":
            {"2017":  [0.25]},
        "_II_brk4":
            {"2017": [[112500, 225000, 112500, 112500, 225000]]},
        "_II_rt5":
            {"2017": [0.25]},
        "_II_brk5":
            {"2017":  [[112500, 225000, 112500, 112500, 225000]]},
        "_II_rt6":
            {"2017": [0.25]},
        "_II_brk6":
            {"2017": [[112500, 225000, 112500, 112500, 225000]]},
        "_II_rt7":
            {"2017": [0.33]},
        "_PT_rt1":
            {"2017": [0.12]},
        "_PT_brk1":
            {"2017": [[37500, 75000, 37500, 37500, 75000]]},
        "_PT_rt2":
            {"2017": [0.15]},
        "_PT_brk2":
            {"2017": [[112500, 225000, 112500, 112500, 225000]]},
        "_PT_rt3":
            {"2017": [0.15]},
        "_PT_brk3":
            {"2017": [[112500, 225000, 112500, 112500, 225000]]},
        "_PT_rt4":
            {"2017": [0.15]},
        "_PT_brk4":
            {"2017": [[112500, 225000, 112500, 112500, 225000]]},
        "_PT_rt5":
            {"2017": [0.15]},
        "_PT_brk5":
            {"2017": [[112500, 225000, 112500, 112500, 225000]]},
        "_PT_rt6":
            {"2017": [0.15]},
        "_PT_brk6":
            {"2017": [[112500, 225000, 112500, 112500, 225000]]},
        "_PT_rt7":
            {"2017": [0.15]},
        "_CG_brk1":
            {"2017": [[37500, 75000, 37500, 37500, 75000]]},
        "_CG_brk2":
            {"2017": [[112500, 225000, 112500, 112500, 225000]]},
        "_AMT_rt1":
            {"2017": [0]},
        "_AMT_rt2":
            {"2017": [0]},
        "_NIIT_rt":
            {"2017": [0]},
        "_STD":
            {"2017": [[15000, 30000, 15000, 15000, 30000]]},
        "_II_em":
            {"2017": [0]},
        "_ALD_Dependents_thd":
            {"2017": [[250000, 500000, 250000, 500000, 500000]]},
        "_ALD_Dependents_Elder_c":
            {"2017": [5000]},
        "_ALD_Dependents_Child_c":
            {"2017": [7156]},
        "_ID_c":
            {"2017": [[100000, 200000, 100000, 100000, 200000]]}
    }
}

// Note: Due to lack of detail, data, or modeling capability, many provisions cannot be scored.
// These omitted provisions include:
// -  Allow expenssing for pass-through firms
// -  Tax carried interest as ordinary business income
// -  Repeal pass-through business tax expenditures
// -  Corporate tax provisions
// -  Estate tax provisions"""

regression_sample_reform = """// Assume reform with the following provisions:
// - adhoc raises in OASDI maximum taxable earnings in 2018, 2019 and 2020,
//     with _SS_Earnings_c wage indexed in subsequent years
// - raise personal exemption amount _II_em in 2018, keep it unchanged for
//     two years and then resume its price indexing in subsequent years
// - implement a 20% investment income AGI exclusion beginning in 2019
{
    "policy": {
        "_SS_Earnings_c": {"2018": [400000],
                           "2019": [500000],
                           "2020": [600000]},
        "_II_em": {"2018": [8000]},
        "_II_em_cpi": {"2018": false,
                       "2020": true},
        "_ALD_InvInc_ec_rt": {"2019": [0.20]}
    }
}"""

bad_reform = """// bad-reform.json contains a logically incorrect attempt to completely
// eliminate the income tax (leaving refundable credits unchanged)
{
    "policy": {
        "_II_rt1": {"2020": [0.0]},
        "_II_brk1": {"2020": [[9e99, 9e99, 9e99, 9e99, 9e99]]},
        "_CG_rt1": {"2020": [0.0]},
        "_CG_rt2": {"2020": [0.0]},
        "_CG_rt3": {"2020": [0.0]},
        "_CG_rt4": {"2020": [0.0]},
        "_AMT_rt1": {"2020": [0.0]},
        "_AMT_rt2": {"2020": [0.0]},
        "_AMT_CG_rt1": {"2020": [0.0]},
        "_AMT_CG_rt2": {"2020": [0.0]},
        "_AMT_CG_rt2": {"2020": [0.0]},
        "_AMT_CG_rt3": {"2020": [0.0]},
        "_AMT_CG_rt4": {"2020": [0.0]}
    }
}
"""

warning_reform = """
// throws warning but not error
{
    "policy": {
        "_STD_single": {"2020": [1000]}
    }
}
"""
