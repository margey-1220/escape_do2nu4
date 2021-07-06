import streamlit as st

from kaitou_bon import kaitou_bon


def main():
    page = kaitou_bon.KaitouBon()
    page.start()

if __name__ == '__main__':
    main()
