import marimo

__generated_with = "0.12.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""# Webassembly Chat App""")
    return


@app.cell
def _(mo):
    def simple_echo_model(messages, config):
        return f"You said: {messages[-1].content}"

    mo.ui.chat(
        simple_echo_model,
        prompts=["Hello", "How are you?"],
        show_configuration_controls=True,
    )

    return (simple_echo_model,)


if __name__ == "__main__":
    app.run()
