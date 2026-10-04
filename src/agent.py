from langgraph.graph import MessagesState

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from src.tools import search_documents, calculator



tools = [search_documents, calculator]

model = ChatOllama(
    model="llama3.2"
).bind_tools(tools)

def call_model(state: MessagesState):
    response = model.invoke(state["messages"])

    return {
        "messages": [response]
    }

graph = StateGraph(MessagesState)

graph.add_node("llm", call_model)
graph.add_node("tools", ToolNode(tools))
graph.add_edge(START, "llm")
def should_continue(state: MessagesState):
    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return "end"

graph.add_conditional_edges(
    "llm",
    should_continue,
    {
        "tools": "tools",
        "end": END
    }
)
graph.add_edge("tools", "llm")
app = graph.compile()

while True:
    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    try:
        result = app.invoke({
            "messages": [
                
                HumanMessage(content=question)
            ]
        })

        print("\nAnswer:")
        print(result["messages"][-1].content)

    except Exception as e:
        print("\nSomething went wrong.")
        print("Error:", e)