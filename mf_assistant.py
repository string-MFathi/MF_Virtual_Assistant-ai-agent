import os
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import Agent, Runner
from tools import read_directory, write_email_draft

# تحميل مفتاح الـ API
load_dotenv()

# ==========================================
# 1. التعليمات (البرومبت) داخل متغيرات بايثون
# ==========================================
base_instructions = """
You are MF_Assistant, a virtual assistant to Mohamed Fathi (an AI Agent Developer).
Always be concise, professional, and accurate.
"""

planner_instructions = """
You are the Planner Agent.
Break down the user's request. You have read-only tools to gather info.
Decide if an action (like writing an email) is required, and write strict instructions for the Executor.
"""

executor_instructions = """
You are the Executor Agent.
Your ONLY job is to execute the instructions given by the Planner Agent using your tools.
Do not ask questions, just execute.
"""

# ==========================================
# 2. الهيكل الإجباري للمخرجات (Structured Output)
# ==========================================
# هنا نستخدم Pydantic لإجبار الوكيل الأول أن يرد علينا بهذا الشكل فقط
class PlannerOutput(BaseModel):
    execution_required: bool
    executor_instructions: str
    user_note: str

# ==========================================
# 3. بناء الوكلاء (Agents Setup)
# ==========================================
# وكيل التخطيط
# وكيل التخطيط
planner_agent = Agent(
    name="Planner Agent",
    instructions=base_instructions + planner_instructions,
    tools=[read_directory],
    output_type=PlannerOutput
)

# وكيل التنفيذ
executor_agent = Agent(
    name="Executor Agent",
    instructions=base_instructions + executor_instructions,
    tools=[write_email_draft]
)
# ==========================================
# 4. دورة العمل (The Workflow)
# ==========================================
def main():
    print("\n🤖 MF_Virtual_Assistant is ready!")
    user_request = "Check the directory for meeting notes and send a follow-up email to client@tech.com"
    print(f"User Request: {user_request}\n")
    
    print("🧠 [Planner] is thinking...")
    # تشغيل وكيل التخطيط
    planner_result = Runner.run_sync(planner_agent, user_request)
    planner_data = planner_result.final_output # هذه البيانات ستكون بنفس هيكل Pydantic
    
    print(f"📝 Planner Note: {planner_data.user_note}")
    print(f"⚡ Execution Required? {planner_data.execution_required}")
    print("-" * 40)
    
    # إذا قرر المخطط أن هناك حاجة للتنفيذ، نشغل وكيل التنفيذ
    if planner_data.execution_required:
        print("⚙️ [Executor] is taking action...")
        
        # نمرر تعليمات المخطط إلى المنفذ
        executor_result = Runner.run_sync(executor_agent, planner_data.executor_instructions)
        print(f"✅ Executor Result: {executor_result.final_output}")
    
    print("\n🎉 Workflow Completed!")

if __name__ == "__main__":
    main()