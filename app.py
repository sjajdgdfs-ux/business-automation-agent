import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src.orchestrator import run
from src.core.schemas import AgentState
st.set_page_config(page_title='Business Agent', page_icon='📊', layout='wide')
st.markdown('''<style>
.agent-box { padding:12px 16px; border-radius:8px; margin:6px 0; font-size:15px; }
.agent-waiting { background:#f0f0f0; color:#888; }
.agent-running { background:#fff8e1; color:#f57c00; }
.agent-done    { background:#e8f5e9; color:#2e7d32; }
.agent-error   { background:#ffebee; color:#c62828; }
</style>''', unsafe_allow_html=True)
def agent_box(label, status, detail=''):
    icons = {'waiting':'⏳','running':'🔄','done':'✅','error':'❌'}
    icon = icons.get(status,'⏳')
    detail_html = f'<br><small>{detail}</small>' if detail else ''
    return f'<div class="agent-box agent-{status}">{icon} <b>{label}</b>{detail_html}</div>'
st.markdown('# 📊 Business Automation Agent')
st.markdown('Upload any **CSV or Excel** file and get a full business intelligence report instantly.')
st.divider()
uploaded = st.file_uploader('Upload your data file', type=['csv','xlsx','xls'])
if uploaded:
    st.success(f'✅ File loaded: {uploaded.name}')
    col1, col2 = st.columns([3,1])
    with col2:
        start = st.button('🚀 Generate Report', use_container_width=True)
    if start:
        col1, col2 = st.columns(2)
        with col1:
            reader_slot  = st.empty()
            analyst_slot = st.empty()
        with col2:
            advisor_slot = st.empty()
            writer_slot  = st.empty()
        reader_slot .markdown(agent_box('📂 Reader',  'waiting'), unsafe_allow_html=True)
        analyst_slot.markdown(agent_box('📊 Analyst', 'waiting'), unsafe_allow_html=True)
        advisor_slot.markdown(agent_box('💡 Advisor', 'waiting'), unsafe_allow_html=True)
        writer_slot .markdown(agent_box('✍️ Writer',  'waiting'), unsafe_allow_html=True)
        reader_slot.markdown(agent_box('📂 Reader', 'running', 'Reading file...'), unsafe_allow_html=True)
        import time
        content = uploaded.read()
        state = run(uploaded.name, content)
        reader_slot .markdown(agent_box('📂 Reader',  'done', f'{state.summary.rows} rows, {state.summary.columns} cols'), unsafe_allow_html=True)
        analyst_slot.markdown(agent_box('📊 Analyst', 'done', 'Analysis complete'), unsafe_allow_html=True)
        advisor_slot.markdown(agent_box('💡 Advisor', 'done', 'Recommendations ready'), unsafe_allow_html=True)
        writer_slot .markdown(agent_box('✍️ Writer',  'done', 'Report written'), unsafe_allow_html=True)
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric('Rows',    state.summary.rows)
        c2.metric('Columns', state.summary.columns)
        c3.metric('Status',  '✅ Complete')
        with st.expander('📊 Raw Analysis', expanded=False):
            st.markdown(state.analysis)
        with st.expander('💡 Recommendations', expanded=False):
            st.markdown(state.advice)
        st.divider()
        st.markdown('## 📄 Final Report')
        st.markdown(state.final_report)
        st.divider()
        st.download_button('⬇️ Download as Markdown', state.final_report, file_name=f'{uploaded.name}_report.md', mime='text/markdown', use_container_width=True)
