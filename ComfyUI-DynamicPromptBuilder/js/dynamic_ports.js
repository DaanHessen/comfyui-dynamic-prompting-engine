import { app } from "../../scripts/app.js";

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
                            const inner = match[1];
                            const parts = inner.split('|');
                            for (const p of parts) {
                                if (p) variables.add(p);
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
        }
    }
});
