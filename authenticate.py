import streamlit as st
import streamlit_authenticator as stauth
import yaml


class Authenticate:
    """this class is the authentication procedures for all the pages in this streamlit app
    """
    def load_yaml(self):
        with open('./config.yaml') as file:
            config = yaml.safe_load(file)

        return config

    def save_yaml(self,config):
        with open('../config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)