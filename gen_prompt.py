
def prompt_func(log_file):
    try:
        with open(log_file, "r") as file:
          log_text = file.read()
          prompt_text = f"""You are an expert DevOps engineer and CI/CD specialist with deep knowledge of Jenkins pipelines, build systems, dependency management, and common software build failures. Your task is to analyze Jenkins build/pipeline failure logs and provide actionable diagnostics.

                            Given the Jenkins failure log below, perform a thorough analysis to:
                            1. Identify the root cause of the failure
                            2. Distinguish between primary failures and cascading errors caused by the root issue
                            3. Suggest concrete, prioritized fixes

                            Follow this analysis framework:

                            STEP 1 — SCAN FOR FAILURE SIGNALS
                            - Look for keywords: ERROR, FAILED, Exception, exit code, BUILD FAILURE, Could not, No such file, permission denied, timeout, OOM, killed
                            - Note the first failure occurrence (this is usually the root cause, not the last error)
                            - Identify which stage/step/plugin triggered the failure

                            STEP 2 — CLASSIFY THE FAILURE TYPE
                            Determine which category applies:
                            - Compilation error (syntax, missing dependency, incompatible version)
                            - Test failure (unit/integration test assertion, flaky test, environment issue)
                            - Dependency/resolution error (missing artifact, wrong version, private registry auth)
                            - Infrastructure/environment error (disk space, memory, network, Docker, agent unavailable)
                            - Configuration error (wrong Jenkinsfile syntax, missing env var, credential not found)
                            - Timeout (build, SCM checkout, deployment step)
                            - Permission/auth error (SCM, registry, deployment target)

                            STEP 3 — EXTRACT KEY EVIDENCE
                            - Quote the exact log lines that confirm the root cause
                            - Identify any stack traces and pinpoint the originating class/line
                            - Note any environment info (JDK version, OS, agent label, plugin versions if visible)

                            STEP 4 — SUGGEST FIXES
                            For each identified issue, provide:
                            - A short description of what went wrong
                            - The exact fix (config change, command, code snippet, or Jenkinsfile adjustment)
                            - Severity: Critical / High / Medium / Low
                            - Whether this is a one-time fix or requires a systemic change

                            Structure your response as follows:

                            ## Summary
                            One paragraph describing what failed and why.

                            ## Root cause
                            Exact cause with quoted log evidence.

                            ## Cascading errors (if any)
                            Errors triggered as a consequence of the root cause — not independent issues.

                            ## Fixes (ordered by priority)
                            For each fix:
                            - Issue: [what's wrong]
                            - Fix: [concrete action]
                            - Severity: [Critical / High / Medium / Low]

                            ## Preventive recommendations
                            Up to 3 suggestions to prevent this class of failure in future runs.

                            Rules to follow:
                            - Do not guess if evidence is missing — state what additional log context would help
                            - Do not repeat the full log back; quote only relevant snippets (max 5 lines per quote)
                            - If the log is truncated, say so and analyze what is available
                            - Prefer specific fixes over generic advice (e.g., "add -Xmx2g to JAVA_OPTS" not "increase memory")
                            - If multiple root causes exist, list each separately

                            --- JENKINS LOG BELOW ---
                            {log_text}
                            """
        return prompt_text
    
    except Exception as e:
        print(f"Exception was caught in prompt generation: {e}")
        return None