from modules.fuzzer_sim import ProtocolFuzzer
from modules.llm_patcher import LLMPatchSynthesizer
from modules.validator import RegressionValidator

def main():
    print("==================================================")
    print("   PRAHAAR KAVACH: Autonomous CRS Pipeline Init   ")
    print("==================================================")

    fuzzer = ProtocolFuzzer(target_protocol_name="Tactical-C2-UDP-Stream")
    fuzz_result = fuzzer.run_fuzzing_cycle()
    print(f"-> Fuzzing Result: {fuzz_result['status']}\n")

    if fuzz_result['status'] == 'VULNERABILITY_FOUND':
        patcher = LLMPatchSynthesizer()
        generated_patch = patcher.generate_patch(fuzz_result['log'])
        print(f"\n-> Synthesized Secure Patch:\n{generated_patch}\n")

        validator = RegressionValidator(generated_patch)
        validation_result = validator.run_sandbox_tests()
        print(f"\n-> Verification Status: {validation_result['message']}")
        print("==================================================")
        print("   Pipeline Cycle Completed Successfully.         ")
        print("==================================================")
    else:
        print("-> Target system is stable. Continuing surveillance loop.")

if __name__ == "__main__":
    main()