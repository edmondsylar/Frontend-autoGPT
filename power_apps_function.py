import streamlit as st

public_holidays = [{
            "Title": "Christmas Holiday",
            "StartDate": "2023-12-25",
            "EndDate": "2023-12-25",
        }, 
        {
            "Title": "Boxing Day",
            "StartDate": "2023-12-26",
            "EndDate": "2023-12-25",
        }]
weekends = []

leave_days = []
leave_balance = []

def add_holiday(holiday):
    public_holidays.append(holiday)

def add_weekend(weekend):
    weekends.append(weekend)

def leave_request(_from, _to):
    pass


# leave dashboard

def leave_application():
    st.subheader("aBi Leave App")

    col_1, col_2 = st.columns([0.3, 0.7])

    with col_1:
        # create a form to request leave.
        with st.form(key="leave_form"):
            date_from = st.date_input("From", key="date_from")
            date_to = st.date_input("Date To:", key="date_to")
            submit = st.form_submit_button(label="Submit Request")

            if submit:
                st.write(f" requested for leave from {date_from} to {date_to}")
                # leave_request(date_from, date_to)

    with col_2:
        # Tabs
        tab_1, tab_2 = st.tabs(["Public Holidays", "Weekends"])

        with tab_1:
            st.write("Public Holidays")
            for holiday in public_holidays:
                st.write(holiday)

        with tab_2:
            st.write("Weekends")
            for weekend in weekends:
                st.write(weekend)

        st.subheader("Personal Leave Details")
        st.markdown("---")


leave_application()

def _test():
    array = [
        {
            "Title": "Christmas Holiday",
            "StartDate": "2023-12-25",
            "EndDate": "2023-12-25",
        }, 
        {
            "Title": "Boxing Day",
            "StartDate": "2023-12-26",
            "EndDate": "2023-12-25",
        }
    ]