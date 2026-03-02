import streamlit as st

st.header("Appendix")

if "prd" in st.session_state:
    # This is a placeholder for the appendix content.
    # In a real application, you would parse the PRD and extract the appendix.
    st.markdown("### Meeting Notes")
    st.markdown("- Item 1\n- Item 2\n- Item 3")
    st.markdown("### Action Items")
    st.markdown("- **Action Item 1:** Owner, Due Date\n- **Action Item 2:** Owner, Due Date")
else:
    st.warning("Please generate a PRD first.")