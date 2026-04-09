import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

app.registerExtension({
    name: "DynamicTemplatePromptBuilder",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "DynamicPromptBuilder") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                if (onNodeCreated) {
                    onNodeCreated.apply(this, arguments);
                }

                const node = this;
                const templateWidget = node.widgets.find(w => w.name === "template");

                if (templateWidget) {
                    const updatePorts = () => {
                        const text = templateWidget.value || "";
                        const regex = /\{([^}]+)\}/g;
                        const variables = new Set();
                        let match;
                        while ((match = regex.exec(text)) !== null) {
                            let inner = match[1];
                            if (inner.includes("$$")) {
                                inner = inner.split("$$").slice(1).join("$$");
                            }
                            const parts = inner.split('|');
                            for (let p of parts) {
                                if (p.includes("::")) {
                                    p = p.split("::").slice(1).join("::");
                                }
                                p = p.trim();
                                if (p && !p.match(/^__[a-zA-Z0-9_\-]+__$/)) {
                                    variables.add(p);
                                }
                            }
                        }

                        const currentInputs = node.inputs || [];
                        const currentInputNames = new Set(currentInputs.map(i => i.name));

                        for (const v of variables) {
                            if (!currentInputNames.has(v)) {
                                node.addInput(v, "STRING");
                            }
                        }

                        for (let i = currentInputs.length - 1; i >= 0; i--) {
                            const input = currentInputs[i];
                            if (!variables.has(input.name)) {
                                node.removeInput(i);
                            }
                        }
                    };

                    const originalCallback = templateWidget.callback;
                    templateWidget.callback = function (value, ...args) {
                        if (originalCallback) {
                            originalCallback.apply(this, [value, ...args]);
                        }
                        updatePorts();
                    };

                    setTimeout(() => {
                        updatePorts();
                    }, 10);
                }
            };

            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                if (onExecuted) {
                    onExecuted.apply(this, arguments);
                }

                if (message && message.text) {
                    const text = message.text[0];
                    let outputWidget = this.widgets.find(w => w.name === "Output");

                    if (!outputWidget) {
                        const w = ComfyWidgets["STRING"](this, "Output", ["STRING", { multiline: true }], app);
                        outputWidget = w.widget || this.widgets.find(w => w.name === "Output");
                        if (outputWidget && outputWidget.inputEl) {
                            outputWidget.inputEl.readOnly = true;
                            outputWidget.inputEl.style.opacity = 0.6;
                        }
                    }

                    if (outputWidget) {
                        outputWidget.value = text;
                        if (outputWidget.inputEl) {
                            outputWidget.inputEl.value = text;
                        }
                    }

                    if (!this.flags?.collapsed) {
                        const sz = this.computeSize();
                        if (sz[0] < this.size[0]) {
                            sz[0] = this.size[0];
                        }
                        if (sz[1] < this.size[1]) {
                            sz[1] = this.size[1];
                        }
                        this.size = sz;
                        if (this.onResize) {
                            this.onResize(this.size);
                        }
                    }

                    this.setDirtyCanvas(true, true);
                }
            };
        }
    }
});
