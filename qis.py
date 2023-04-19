from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram

# 量子回路を作成（1つの量子ビットと1つの古典ビットを持つ）
qc = QuantumCircuit(1, 1)

# 量子重ね合わせを実現するアダマールゲートを量子ビットに適用（インデックス0の量子ビットに適用）
qc.h(0)

# 測定操作を行う
# 量子ビットを古典ビットにマップ（インデックス0の量子ビットをインデックス0の古典ビットにマップ）
qc.measure(0, 0)

# 回路を表示
print(qc)

# シミュレータを選択（Aer.get_backend('qasm_simulator')はユニバーサルな量子コンピュータシミュレータです）
simulator = Aer.get_backend('qasm_simulator')

# トランスパイルと実行（シミュレーション）の準備
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit, shots=1024)

# シミュレーション実行
result = simulator.run(qobj).result()

# 結果を取得して表示
counts = result.get_counts(qc)
print("Result: ", counts)
plot_histogram(counts).show()
