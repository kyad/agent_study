# https://qiita.com/tinymouse/items/2e22b655d8ba5fe6f3b3

import langchain_ollama
import langchain_core.prompts
import langchain.agents
import mcp
import langchain_mcp_adapters.tools
import asyncio


async def main():

    model = langchain_ollama.OllamaLLM(
        model="gemma4"
    )

    prompt = langchain_core.prompts.chat.ChatPromptTemplate.from_template(
        """Question: {input}
        Thought: Let's think step by step.
        Use one of registered tools to answer the question.
        Answer: {agent_scratchpad}"""
    )

    params = mcp.StdioServerParameters(
        command="uv",
        args=["run", "mcp_srv.py"],
    )

    async with mcp.client.stdio.stdio_client(params) as (read, write):
        async with mcp.ClientSession(read, write) as session:
            await session.initialize()
            tools = await langchain_mcp_adapters.tools.load_mcp_tools(session)

            # agent = langchain.agents.create_tool_calling_agent(model, tools, prompt)
            # executor = langchain.agents.AgentExecutor(agent=agent, tools=tools)

            # query = "なごや個人開発者の集いとは何ですか？"

            # output = await executor.ainvoke({"input": query})

            agent = langchain.agents.create_agent(
                model="ollama:gemma4",
                tools=tools,
                system_prompt="You are a helpful assistant.",
            )

            result = await agent.ainvoke(
                {"messages": [{"role": "user", "content": "なごや個人開発者の集いとは何ですか？"}]}
            )
            output = result["messages"][-1].content_blocks

            print(output)


asyncio.run(main())
