import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
with open("css/style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

# try:
    last_update = pd.read_csv("data/last_update.csv")
    st.markdown("Terakhir Update " + last_update["0"][0])
    repo = pd.read_csv("data/repo.csv")
    wilkerstat = pd.read_csv("data/wilkerstat.csv")

    if wilkerstat["nm_project"][0].astype(str).startswith("000"):
        wilkerstat['idsubsls'] = wilkerstat['iddesa'].astype(
            str)+wilkerstat['nm_project'].astype(str)
    else:
        wilkerstat['idsubsls'] = wilkerstat['iddesa'].astype(
            str)+"000"+wilkerstat['nm_project'].astype(str)
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown("Jumlah SLS/Non SLS Repo")
    col1.markdown(len(repo))
    col2.markdown("Jumlah UTP (R305) Repo")
    col2.markdown(sum(repo['b305']))
    col3.markdown("Jumlah Project Wilkerstat")
    col3.markdown(len(wilkerstat.groupby('idsubsls').count()))
    col4.markdown("Jumlah ART Pertanian")
    col4.markdown(sum(wilkerstat['jumlah_art_tani']))

    wilkerstat_sum = wilkerstat.groupby(['idsubsls'])['jumlah_art_tani'].sum()
    wilkerstat_count = wilkerstat.groupby(
        ['idsubsls'])['jumlah_art_tani'].count()
    wilkerstat_subsls = pd.DataFrame(
        {'jumlah_tagging': wilkerstat_count, 'jumlah_art_tani': wilkerstat_sum})
    wilkerstat_subsls.index.name = 'idsubsls'
    wilkerstat_subsls.reset_index(inplace=True)
    repo_subsls = pd.DataFrame(repo.iloc[:, [0, 7, 22, 25]])
    repo_subsls['idsubsls'] = repo_subsls['idsubsls'].astype(str)
    wilkerstat_subsls['idsubsls'] = wilkerstat_subsls['idsubsls'].astype(str)
    wilkerstat_subsls['jumlah_tagging'] = wilkerstat_subsls['jumlah_tagging'].astype(
        int)
    wilkerstat_subsls['jumlah_art_tani'] = wilkerstat_subsls['jumlah_art_tani'].astype(
        int)
    st.table(repo_subsls.merge(wilkerstat_subsls, how="left", on='idsubsls'))
# except:
#     st.markdown("Data Belum di update")
