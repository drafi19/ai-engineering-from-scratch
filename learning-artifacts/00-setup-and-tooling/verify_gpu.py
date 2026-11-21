"""Verify the GPU actually computes - not just that torch imports.

Run:  .venv\Scripts\python.exe verify_gpu.py
"""

import time

import torch

print("=== Build info ===")
print(f"torch        : {torch.__version__}")
print(f"cuda built   : {torch.version.cuda}")
print(f"cuda available: {torch.cuda.is_available()}")

if not torch.cuda.is_available():
    print("\nNo CUDA device. The course still works on CPU for phases 0-3, 5, 7-11.")
    raise SystemExit(1)

print(f"device count : {torch.cuda.device_count()}")
props = torch.cuda.get_device_properties(0)
print(f"device       : {props.name}")
print(f"compute cap  : sm_{props.major}{props.minor}")
print(f"VRAM total   : {props.total_memory / 1024**3:.2f} GB")
print(f"torch archs  : {torch.cuda.get_arch_list()[:12]}")

print("\n=== Matmul on GPU vs CPU ===")
n = 2048
a_cpu = torch.randn(n, n)
b_cpu = torch.randn(n, n)

# CPU
t0 = time.perf_counter()
c_cpu = a_cpu @ b_cpu
cpu_ms = (time.perf_counter() - t0) * 1000

# GPU (with warmup, since the first kernel triggers JIT/module load)
a_gpu = a_cpu.cuda()
b_gpu = b_cpu.cuda()
torch.cuda.synchronize()
_ = a_gpu @ b_gpu
torch.cuda.synchronize()

t0 = time.perf_counter()
c_gpu = a_gpu @ b_gpu
torch.cuda.synchronize()
gpu_ms = (time.perf_counter() - t0) * 1000

print(f"CPU {n}x{n} matmul : {cpu_ms:8.1f} ms")
print(f"GPU {n}x{n} matmul : {gpu_ms:8.1f} ms")
print(f"speedup            : {cpu_ms / gpu_ms:8.2f}x")

# Correctness: the GPU result must actually match the CPU result.
max_err = (c_cpu - c_gpu.cpu()).abs().max().item()
print(f"max abs error      : {max_err:.2e}")

print("\n=== Tiny training step (real backward pass) ===")
torch.manual_seed(0)
model = torch.nn.Sequential(
    torch.nn.Linear(64, 128),
    torch.nn.ReLU(),
    torch.nn.Linear(128, 10),
).cuda()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
x = torch.randn(256, 64, device="cuda")
y = torch.randint(0, 10, (256,), device="cuda")

t0 = time.perf_counter()
for _ in range(50):
    loss = torch.nn.functional.cross_entropy(model(x), y)
    opt.zero_grad()
    loss.backward()
    opt.step()
torch.cuda.synchronize()
step_ms = (time.perf_counter() - t0) * 1000 / 50

print(f"loss after 50 steps: {loss.item():.4f}")
print(f"per step           : {step_ms:.2f} ms")
print(f"peak VRAM used     : {torch.cuda.max_memory_allocated() / 1024**2:.0f} MB")

print("\nGPU is working. CUDA training is available for this course.")
